import axios from "axios";
import { debounce } from "lodash";
import Select, { MultiValue } from "react-select";
import ReactJson from "@microlink/react-json-view";
import {
  useState,
  useEffect,
  ChangeEvent,
  useCallback,
} from "react";
import { AgGridReact } from "ag-grid-react";
import { ColDef } from "ag-grid-community";
import { MagnifyingGlass } from "react-loader-spinner";
import { API_BASE_URL } from "../constants/config";

interface Log {
  level: string;
  message: string;
  resourceId: string;
  timestamp: string;
}

interface ApiResponse {
  hits: {
    hits: Array<{ _source: Log }>;
  };
}

export interface LogFilterOption {
  value: string;
  label: string;
}
const LogLevelOptions: LogFilterOption[] = [
  { value: "error", label: "Error" },
  { value: "warning", label: "Warning" },
  { value: "info", label: "Info" },
];

const LogDashboard = () => {
  const [rowData, setRowData] = useState<Log[]>([]);
  const [loading, setLoading] = useState(true);

  const [searchAllText, setSearchAllText] = useState("");
  const [searchCommitText, setSearchCommitText] = useState("");

  const [selectedLogLevels, setSelectedLogLevels] = useState<
    MultiValue<LogFilterOption>
  >([]);

  // Debounce the API call function to avoid making too many API calls for every key press
  const debouncedSearch = useCallback(
    debounce((query: string) => {
      setLoading(true);

      const searchQuery = {
        text: query,
        filters: [
          {
            columnName: "level",
            filterValues: selectedLogLevels.map((option) => option.value),
          },
          {
            columnName: "commit",
            filterValues: null
          },
        ],
      };
      console.log("Initiate API call with search query:", query, searchQuery);

      axios
        .post<ApiResponse>(`${API_BASE_URL}/search-logs`, searchQuery)
        .then((response) => {
          setRowData(response.data.hits.hits.map((hit) => hit._source));
          setLoading(false);
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
          setLoading(false);
        });
    }, 200),
    [selectedLogLevels, setLoading, setRowData]
  );

  // Event handler for input change
  const handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
    setSearchAllText(event.target.value);
    debouncedSearch(event.target.value);
  };

  // Event handler for input blur
  const handleInputBlur = () => {
    debouncedSearch.cancel(); // Cancel any pending API calls
    // Perform API call with the current search text
    debouncedSearch(searchAllText);
  };

  // Event handler for Enter key press
  const handleInputKeyUp = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter") {
      debouncedSearch.cancel(); // Cancel any pending API calls
      // Perform API call with the current search text
      debouncedSearch(searchAllText);
    }
  };

  useEffect(() => {
    debouncedSearch(searchAllText);
  }, [selectedLogLevels]);

  const defaultColDef: ColDef = {
    sortable: true,
    resizable: true,
    autoHeight: true,
    wrapHeaderText: true,
  };

  const columnDefs: ColDef[] = [
    { headerName: "Level", field: "level", width: 100 },
    { headerName: "Message", field: "message", width: 300 },
    { headerName: "Resource ID", field: "resourceId" },
    { headerName: "Trace ID", field: "traceId" },
    { headerName: "Span ID", field: "spanId" },
    { headerName: "Commit", field: "commit", width: 100 },
    { headerName: "Parent resource ID", field: "parentResourceId" },
    { headerName: "Metadata", field: "metadata", width: 300, cellRenderer: (props: any) => (
      <ReactJson
          src={props.value}
          enableClipboard={false}
          displayDataTypes={false}
          collapsed={0}
          style={{ overflowX: "auto", lineHeight: 1.5 }}
        />
    )},
    { headerName: "Timestamp", field: "timestamp" },
  ];

  return (
    <div className="m-2 w-100 p-0 bg-gray-100 rounded shadow-lg">
      <h2 className="text-center text-2xl font-bold mb-4">
        <img
          src={`${process.env.PUBLIC_URL}/logo512.png`}
          alt="Logo"
          className="inline-block mr-2 h-8 w-8"
        />
        Logs Dashboard
      </h2>
      <div className="mb-4">
        <input
          type="text"
          placeholder="Search by any field :)"
          className="p-2 border rounded w-2/12"
          value={searchAllText}
          onChange={handleInputChange}
          onBlur={handleInputBlur}
          onKeyUp={handleInputKeyUp}
        />
        <Select
          isMulti
          options={LogLevelOptions}
          value={selectedLogLevels}
          onChange={setSelectedLogLevels}
          placeholder="Select log levels..."
          className="mx-2 w-3/12 inline-block"
        />
      </div>
      <div
        className="ag-theme-alpine"
        style={{ height: "80vh", width: "100%" }}
      >
        <AgGridReact
          defaultColDef={defaultColDef}
          columnDefs={columnDefs}
          enableCellTextSelection
          rowData={loading ? null : rowData}
          pagination={true}
          paginationPageSize={100}
          loadingOverlayComponent={() => (
            <div className="flex">
              <MagnifyingGlass
                visible={true}
                height="80"
                width="80"
                ariaLabel="MagnifyingGlass-loading"
                wrapperStyle={{}}
                wrapperClass="MagnifyingGlass-wrapper"
                glassColor="#c0efff"
                color="#e15b64"
              />
            </div>
          )}
        />
      </div>
    </div>
  );
};

export default LogDashboard;
