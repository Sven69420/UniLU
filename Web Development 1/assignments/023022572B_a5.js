function makeSortable(table) { 
  // Variables to keep track of the current sorting state
  let currentColumn = -1;
  let ascending = true;

  // Function to sort the table rows based on the selected column and order
  function sortTable(columnIndex, isAscending) {
    // Get the table body and convert rows into array
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.rows);

    // Sort the rows based on the content of the selecte columns 
    rows.sort((a, b) => {
      // Extract and trim the text content of the cells in the selected column
      const aVal = a.cells[columnIndex].textContent.trim();
      const bVal = b.cells[columnIndex].textContent.trim();

      // If statement to check wether order should be ascending or descending 
      if (isAscending) {
        // If ascending, use localeCompare for ascending order
        return aVal.localeCompare(bVal);
      } else {
        // If descending, reverse the order for descending order
        return bVal.localeCompare(aVal);
      }
    });

    // Clear the exisitng tbody content and append the sorted rows
    tbody.innerHTML = '';
    rows.forEach(row => tbody.appendChild(row));
  }

  // Function to handle click events on table headers  
  function handleHeaderClick(event) {
    // Get the clicked th element and its index within the rows
    const th = event.target;
    const columnIndex = Array.from(th.parentNode.children).indexOf(th);

    // Updates sorting state based on the clicked colums
    if (currentColumn === columnIndex) {
      // Behaviour for same column click, toggle betweend ascending and descending
      ascending = !ascending;
    } else {
      // If different column clicked, set to ascending and update columns
      currentColumn = columnIndex;
      ascending = true;
    }

    // Call the sorting Function with the current sorting state
    sortTable(currentColumn, ascending);
  }

  // Get all the th elements within the table head and attach a click even listener to it
  const headers = table.querySelectorAll('thead th');
  headers.forEach(header => header.addEventListener('click', handleHeaderClick));
}

// Call the function with html table
const table = document.querySelector('table');
makeSortable(table);