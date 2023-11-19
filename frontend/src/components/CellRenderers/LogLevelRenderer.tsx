import {
  LogLevelOptions,
  UnknownLogLevelOption,
} from "../LogDashboard/LogsTableConfig";

export const LogLevelRenderer = (props: { value: string }) => {
  const { value } = props;

  // Finding the log level configuration based on the provided value
  const logLevel = LogLevelOptions.find((option) => option.value === value);

  // Retrieving badge class and label from the log level configuration, or using defaults from UnknownLogLevelOption
  const badgeClass = logLevel?.badgeClass || UnknownLogLevelOption.badgeClass;
  const label = logLevel?.label || UnknownLogLevelOption.label;

  return (
    <span className={`text-xs font-medium px-2 py-1 prounded ${badgeClass}`}>
      {label}
    </span>
  );
};
