function updateDataNumber(value) {
        var numberElement = document.querySelector('.number');
        var currentNumber = parseInt(numberElement.getAttribute('data-number'), 10);
        var newNumber = currentNumber + value;

        // Set the new data-number attribute and text content
        numberElement.setAttribute('data-number', newNumber);
        numberElement.textContent = newNumber;
    }

    // Example: Increment the data-number by 1 (you can replace this with your donation logic)
    updateDataNumber(1);