import React from "react";
import { useTable } from "react-table";

export default function Table({ columns, data }) {
    // Table component logic and UI come here

    const {
        getTableProps, // table props from react-table
        getTableBodyProps, // table body props from react-table
        headerGroups, // headerGroups if your table have groupings
        rows, // rows for the table based on the data passed
        prepareRow // Prepare the row (this function need to called for each row before getting the row props)
      } = useTable({
        columns,
        data
      });

      /* 
    Render the UI for your table
    - react-table doesn't have UI, it's headless. We just need to put the react-table props from the Hooks, and it will do its magic automatically
  */
  return (
    <table {...getTableProps()}>
      <thead>
        {headerGroups.map(headerGroup => (
          <tr {...headerGroup.getHeaderGroupProps()}>
            {headerGroup.headers.map(column => (
              <th {...column.getHeaderProps()}>{column.render("Header")}</th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody {...getTableBodyProps()}>
      {rows.map((row, i) => {
  prepareRow(row); // This line is necessary to prepare the rows and get the row props from react-table dynamically

  // Each row can be rendered directly as a string using the react-table render method
  return (
    <tr {...row.getRowProps()}>
      {row.cells.map(cell => {
        return <td {...cell.getCellProps()}>{cell.render("Cell")}</td>;
      })}
    </tr>
  );
})}
      </tbody>
    </table>
  );
}

//Search for stock function

// Create a state
const [filterInput, setFilterInput] = useState("");

// Update the state when input changes
const handleFilterChange = e => {
  const value = e.target.value || undefined;
  setFilterInput(value);
};

// Input element
<input
  value={filterInput}
  onChange={handleFilterChange}
  placeholder={"Search name"}
/>


const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    rows,
    prepareRow,
    setFilter // The useFilter Hook provides a way to set the filter
  } = useTable(
    {
      columns,
      data
    },
    useFilters // Adding the useFilters Hook to the table
    // You can add as many Hooks as you want. Check the documentation for details. You can even add custom Hooks for react-table here
  );