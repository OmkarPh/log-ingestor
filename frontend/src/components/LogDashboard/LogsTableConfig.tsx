import { ColDef } from "ag-grid-community";
import { LogFilterOption } from "./LogDashboard.types";
import { LogLevelRenderer } from "../CellRenderers/LogLevelRenderer";
import ReactJson from "@microlink/react-json-view";

export const LogLevelOptions: LogFilterOption[] = [
  { value: "error", label: "Error", badgeClass: "bg-red-100 text-red-800" },
  {
    value: "warning",
    label: "Warning",
    badgeClass: "bg-yellow-100 text-yellow-800",
  },
  { value: "info", label: "Info", badgeClass: "bg-green-100 text-green-800" },
];

export const UnknownLogLevelOption: LogFilterOption = {
  value: "unknown",
  label: "Unknown",
  badgeClass: "bg-gray-100 text-gray-800",
};

export const DefaultColDef: ColDef = {
  sortable: true,
  resizable: true,
  autoHeight: true,
  wrapHeaderText: true,
};

export const LogsTableColumnDefs: ColDef[] = [
  {
    headerName: "Level",
    field: "level",
    width: 100,
    cellRenderer: LogLevelRenderer,
  },
  { headerName: "Message", field: "message", width: 300 },
  { headerName: "Resource ID", field: "resourceId", width: 200 },
  { headerName: "Trace ID", field: "traceId", width: 140 },
  { headerName: "Span ID", field: "spanId", width: 120 },
  { headerName: "Commit", field: "commit", width: 100 },
  {
    headerName: "Parent resource ID",
    field: "metadata",
    width: 160,
    valueFormatter: (props: any) => props.value["parentResourceId"],
  },
  { headerName: "Timestamp", field: "timestamp" },
  {
    headerName: "Metadata",
    field: "metadata",
    width: 400,
    valueFormatter: (props: any) => props,
    cellRenderer: (props: any) => (
      <ReactJson
        src={props.value}
        enableClipboard={false}
        displayDataTypes={false}
        collapsed={0}
        style={{ overflowX: "auto", lineHeight: 1.5, marginTop: "5px" }}
      />
    ),
  },
];
