import React, { useState, KeyboardEventHandler } from "react";
import CreatableSelect from "react-select/creatable";

interface MultiselectTextInputProps {
  placeholder: string;
  updateSelectedOptions: React.Dispatch<
    React.SetStateAction<readonly MultiselectTextInputOption[]>
  >;
  className?: string;
}

export interface MultiselectTextInputOption {
  readonly label: string;
  readonly value: string;
}

const createOption = (label: string) => ({
  label,
  value: label,
});

const MultiselectTextInput: React.FC<MultiselectTextInputProps> = ({
  placeholder,
  className,
  updateSelectedOptions,
}) => {
  const [inputValue, setInputValue] = useState("");
  const [value, setValue] = useState<readonly MultiselectTextInputOption[]>([]);

  const handleKeyDown: KeyboardEventHandler = (event) => {
    if (!inputValue) return;
    switch (event.key) {
      case "Enter":
      case "Tab":
        setValue((prev) => [...prev, createOption(inputValue)]);
        updateSelectedOptions((prev) => [...prev, createOption(inputValue)]);
        setInputValue("");
        event.preventDefault();
    }
  };

  const handleChange = (newValue: readonly MultiselectTextInputOption[]) => {
    setValue(newValue);
    updateSelectedOptions(newValue);
  };

  return (
    <CreatableSelect
      inputValue={inputValue}
      isClearable
      isMulti
      menuIsOpen={false}
      onInputChange={(newValue) => setInputValue(newValue)}
      onKeyDown={handleKeyDown}
      onChange={handleChange}
      placeholder={placeholder}
      className={`m-1 w-3/12 inline-block ${className}`}
      value={value}
    />
  );
};

export default MultiselectTextInput;
