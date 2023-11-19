import axios from "axios";
import { debounce } from "lodash";
import Select, { MultiValue } from "react-select";
import { useState, useEffect, ChangeEvent, useCallback } from "react";
import { AgGridReact } from "ag-grid-react";
import { MagnifyingGlass } from "react-loader-spinner";
import { API_BASE_URL } from "../../constants/config";
import {
  Log,
  LogFilterOption,
  ApiResponse,
  LogFilter,
} from "./LogDashboard.types";
import {
  LogLevelOptions,
  DefaultColDef,
  LogsTableColumnDefs,
} from "./LogsTableConfig";
import { isValidSearchText } from "../../utils/text";
import MultiselectTextInput, {
  MultiselectTextInputOption,
} from "../CustomInputs/MultiselectTextInput";

const LogDashboard = () => {
  const [rowData, setRowData] = useState<Log[]>([]);
  const [loading, setLoading] = useState(true);

  const [searchAllText, setSearchAllText] = useState("");
  const [searchRegexText, setSearchRegexText] = useState("");
  const [startDate, setStartDate] = useState<string>("");
  const [endDate, setEndDate] = useState<string>("");

  const [searchCommitTextOptions, setSearchCommitTextOptions] = useState<
    readonly MultiselectTextInputOption[]
  >([]);
  const [searchSpanIdOptions, setSearchSpanIdOptions] = useState<
    readonly MultiselectTextInputOption[]
  >([]);
  const [searchMessageOptions, setMessageOptions] = useState<
    readonly MultiselectTextInputOption[]
  >([]);
  const [searchResourceIdOptions, setResourceIdOptions] = useState<
    readonly MultiselectTextInputOption[]
  >([]);
  const [searchTraceIdOptions, setTraceIdOptions] = useState<
    readonly MultiselectTextInputOption[]
  >([]);
  const [searchParentResourceIdOptions, setParentResourceIdOptions] = useState<
    readonly MultiselectTextInputOption[]
  >([]);
  const [searchMetadataOptions, setMetadataOptions] = useState<
    readonly MultiselectTextInputOption[]
  >([]);

  const [selectedLogLevels, setSelectedLogLevels] = useState<
    MultiValue<LogFilterOption>
  >([]);

  // Debounce the API call function to avoid making too many API calls for every key press
  // eslint-disable-next-line react-hooks/exhaustive-deps
  const debouncedSearch = useCallback(
    debounce(() => {
      setLoading(true);

      const searchColumnOptions = [
        { columnName: "commit", columnOptions: searchCommitTextOptions },
        { columnName: "spanId", columnOptions: searchSpanIdOptions },
        { columnName: "message", columnOptions: searchMessageOptions },
        { columnName: "resourceId", columnOptions: searchResourceIdOptions },
        { columnName: "traceId", columnOptions: searchTraceIdOptions },
        {
          columnName: "metadata.parentResourceId",
          columnOptions: searchParentResourceIdOptions,
        },
        { columnName: "metadata", columnOptions: searchMetadataOptions },
      ];

      // Include selected log levels in the search filters
      const searchFilters: LogFilter[] = [
        ...(selectedLogLevels.length > 0
          ? [
              {
                columnName: "level",
                filterValues: selectedLogLevels.map((option) => option.value),
              },
            ]
          : []),
        ...searchColumnOptions.flatMap(({ columnName, columnOptions }) =>
          columnOptions.length > 0
            ? [
                {
                  columnName: columnName,
                  filterValues: columnOptions.map((option) => option.value),
                },
              ]
            : []
        ),
      ];

      // Construct the final search query
      const searchQuery = {
        ...(isValidSearchText(searchRegexText) && {
          regexText: searchRegexText,
        }),
        ...(isValidSearchText(searchAllText) && { text: searchAllText }),
        ...(searchFilters.length > 0 && { filters: searchFilters }),
        ...((isValidSearchText(startDate) || isValidSearchText(endDate)) && {
          timeRange: {
            ...(isValidSearchText(startDate) && {
              startTime: new Date(startDate).toISOString(),
            }),
            ...(isValidSearchText(endDate) && {
              endTime: new Date(endDate).toISOString(),
            }),
          },
        }),
      };

      // console.log("Initiate API call with search query:", searchQuery);

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
    [
      selectedLogLevels,
      setLoading,
      setRowData,
      searchAllText,
      searchRegexText,
      searchCommitTextOptions,
      searchSpanIdOptions,
      searchMessageOptions,
      searchResourceIdOptions,
      searchTraceIdOptions,
      searchParentResourceIdOptions,
      searchMetadataOptions,
      startDate,
      endDate,
    ]
  );

  // Event handler for input change
  const handleInputChange = (
    event: ChangeEvent<HTMLInputElement>,
    setTextDispatcher: React.Dispatch<React.SetStateAction<string>>
  ) => {
    setTextDispatcher(event.target.value);
    debouncedSearch();
  };

  // Event handler for Enter key press
  const handleInputKeyUp = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter") {
      // Cancel any pending API calls
      debouncedSearch.cancel();
      debouncedSearch();
    }
  };

  useEffect(() => {
    debouncedSearch.cancel();
    debouncedSearch();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [selectedLogLevels, debouncedSearch]);

  return (
    <div className="m-2 w-100 p-0 bg-gray-100 rounded shadow-lg">
      <div className="">
        <div className="w-full flex -mx-2">
          <input
            type="text"
            placeholder="Search by any field :)"
            className="ml-2 p-2 border rounded w-3/12"
            style={{ height: "38px" }}
            value={searchAllText}
            onChange={(e) => handleInputChange(e, setSearchAllText)}
            onKeyUp={handleInputKeyUp}
          />
          <input
            type="text"
            placeholder="Search using regex"
            className="ml-2 p-2 border rounded w-3/12"
            style={{ height: "38px" }}
            value={searchRegexText}
            onChange={(e) => handleInputChange(e, setSearchRegexText)}
            onKeyUp={handleInputKeyUp}
          />
          <div className="ml-2 w-2/12 ">
            <label htmlFor="startDate" className="mx-2">
              Since
            </label>
            <input
              type="date"
              placeholder="Start Date"
              id="startDate"
              className="m-1inline-block p-2 border rounded"
              value={startDate}
              onChange={(e) => setStartDate(e.target.value)}
            />
          </div>

          <div className="w-2/12 ">
            <label htmlFor="endDate" className="mx-2">
              Till
            </label>
            <input
              type="date"
              placeholder="End Date"
              id="endDate"
              className="m-1 inline-block p-2 border rounded"
              value={endDate}
              onChange={(e) => setEndDate(e.target.value)}
            />
          </div>
        </div>
        <div className="w-full flex -mx-2">
          <MultiselectTextInput
            placeholder={"Filter by commit"}
            updateSelectedOptions={setSearchCommitTextOptions}
          />
          <MultiselectTextInput
            placeholder={"Filter by span id"}
            updateSelectedOptions={setSearchSpanIdOptions}
          />
          <MultiselectTextInput
            placeholder={"Filter by Resource ID"}
            updateSelectedOptions={setResourceIdOptions}
          />
          <MultiselectTextInput
            placeholder={"Filter by Trace ID"}
            updateSelectedOptions={setTraceIdOptions}
          />
        </div>
        <div className="w-full flex -mx-2">
          <Select
            isMulti
            options={LogLevelOptions}
            value={selectedLogLevels}
            onChange={setSelectedLogLevels}
            placeholder="Select log levels..."
            className="mx-2 w-3/12 inline-block"
          />
          <MultiselectTextInput
            placeholder={"Filter by Message"}
            updateSelectedOptions={setMessageOptions}
          />
          <MultiselectTextInput
            placeholder={"Filter by Metadata"}
            updateSelectedOptions={setMetadataOptions}
          />
          <MultiselectTextInput
            placeholder={"Filter by Metadata.ParentResourceID"}
            updateSelectedOptions={setParentResourceIdOptions}
          />
        </div>
      </div>
      <div
        className="ag-theme-alpine"
        style={{ height: "calc(100vh - 170px)", width: "100%" }}
      >
        <AgGridReact
          defaultColDef={DefaultColDef}
          columnDefs={LogsTableColumnDefs}
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
