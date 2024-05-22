function createTOC(domNode) {
    // Create an unordered list element to serve as the Table of Contents (TOC)
    let tOC = document.createElement('ul');
    tOC.id = 'toc'; //assign ID 

    // Retrieving headings (from h2 to h6) within the specified domNode element
    let sectionHeadings = domNode.querySelectorAll('h2, h3, h4, h5, h6');

    // Looping through each heading to populate the table of contents
    for (let index = 0; index < sectionHeadings.length; index++) {
        let currentHeading = sectionHeadings[index];

        // Skip h1 headings
        if (currentHeading.tagName === 'h1') continue;

        // Create list item for each heading
        let tOC_entry = document.createElement('li');
        
        // Assigning a custom attribute to indicate the heading level
        tOC_entry.setAttribute('data-heading', currentHeading.tagName[1]);

        // Linking to the heading if it has an ID; otherwise, just listing its text
        if (currentHeading.id) {
            let tOC_link = document.createElement('a');
            // Set the links hypertext reference to target the headings ID 
            tOC_link.href = `#${currentHeading.id}`;
            // Use the headings text as the link text
            tOC_link.innerText = currentHeading.innerText;
            // Append the link to the list 
            tOC_entry.appendChild(tOC_link);
        } else {
            // Use the heading's text content for the TOC entry if there's no ID present
            tOC_entry.innerText = currentHeading.innerText;
        }

        // Appending the generated item to the table of contents list
        tOC.appendChild(tOC_entry);
    }

    // Return the complete table of contents list
    return tOC;
}