function addCoverage(invoices, coveragePercentage) {
    // Check to see if invoices of coveragePercentage are missing
    if (!invoices || !coveragePercentage) {
        // Gives corresponding Syntax error
        throw new SyntaxError("Missing arguments");
    }

    // Checks if invoices is a valida data type
    if (!Array.isArray(invoices)) {
        // Gives corresponding Type error
        throw new TypeError("Invalid data type");
    }

    // Checks if invoice data or data type are missing or invalid by checking if invoice has no "object" or if type of id and amount are not "string" or "number" types
    for (const invoice of invoices) {
    if (typeof invoice !== 'object' || !invoice.id || typeof invoice.id !== 'string' || !invoice.amount || typeof invoice.amount !== 'number') {
        // Gives corresponing error message
        throw new Error("Missing invoice data or invalid data type");
    }

    // Checks if invoice amount is less than 0
    if (invoice.amount < 0){
        // Gives corresponding Type error
        throw new TypeError("Invalid data type");
    }
    
    // Checks if coveragePercentage is inbetween 0 and 100
    if (coveragePercentage < 0 || coveragePercentage > 100) {
        // Throws corresponding Range error
        throw new RangeError("Coverage percentage must be between 0 and 100");
    }

    // Throws type error if coveragePercentage is not a "number" type
    if (typeof coveragePercentage !== 'number') {
        //Throws corresponding Type error
        throw new TypeError("Invalid data type");
    }
    
    // Copy each invoice to prevent mutation
    let appliedCoverage = JSON.parse(JSON.stringify(invoices));;
    // Calculates coverage for each invoice
    appliedCoverage.forEach(entry => {
        // Coverage equals invoice amount times the coverage percentage
        entry["coverage"] = entry.amount * (coveragePercentage / 100);
    });
    // Returns the applies coverage for each invoice
    return appliedCoverage;
    }
    
}
