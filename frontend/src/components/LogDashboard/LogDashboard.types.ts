export interface LogFilterOption {
  value: string;
  label: string;
  badgeClass: string;
}

export interface Log {
  level: string;
  message: string;
  resourceId: string;
  timestamp: string;
  traceId: string;
  spanId: string;
  commit: string;
  parentResourceId: string;
  metadata: Record<string, string>;
}

export interface LogFilter {
  columnName: string;
  filterValues: string[];
}

export interface ApiResponse {
  hits: {
    hits: Array<{ _source: Log }>;
  };
}
