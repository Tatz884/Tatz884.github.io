const unordList = document.querySelector("ul");
const input = document.querySelector("input");
const addBtn = document.querySelector("#add");
const clearAllBtn = document.querySelector("#clear-all")
const errorText = document.querySelector('#error-text')

let errorType = ""

addBtn.addEventListener("click", () => {
    errorText.textContent = "";
    errorText.className = "";
    const currText = input.value
    if (validateInput()) {
        storeData(currText);
        displayTasks();
    } else {
        showError();
    }
    input.value = '';
    input.focus()
})



function validateInput() {
    // check if form is empty
    if (input.value === '') {
        errorType = "empty"
        return false
    }

    // check if input does not contain any characters
    const regex = /[A-Za-z0-9]+/;
    if (!regex.test(input.value)) {
        errorType = "non-letter"
        return false
    }

    // check if form matches the existing tasks (i.e. creating task duplicates)
    for (var i = 0; i < localStorage.length; i++) {
        if (localStorage.getItem(localStorage.key(i)) === input.value) {
            errorType = "duplicate"
            return false
        }
    }
    
    return true
}

function showError() {
    if (errorType === "empty") {
        errorText.textContent = "Empty tasks are not allowed"
    } else if (errorType === "non-letter") {
        errorText.textContent = "Tasks require at least one alphabet or number"
    } else if (errorType === "duplicate") {
        errorText.textContent = "Duplicated tasks are not allowed"
    } 
    errorText.className = 'error';
}


clearAllBtn.addEventListener("click", () => {
    const currStorageLength = localStorage.length
    // clean all displayed tasks:
    while (unordList.firstChild) {
        unordList.removeChild(unordList.firstChild);
    }
    // remove all tasks in localStorage
    localStorage.clear();
})

function storeData(currText) {
    // store a task written on the form

    console.log(`storing data... localStorage.length = ${localStorage.length}`)

    // store with timestamp
    var d=new Date();
    var timestamp = d.getTime();
    localStorage.setItem(`${timestamp}`, `${currText}`);
    // for example, localStorage should look like:
    // {111111111: "a", 111111113: "b"}


    // Note about this code:
    // Somehow localStorage[`${localStorage.length}`] = currText or
    // localStorage.setItem(localStorage.length) = currText will be executed multiple times and
    // thus are not appropriate here.
    // Since the console.log above is executed only once, storeData triggering seems to be fine.
    // I am not sure if it is a problem of the localStorage.setItem or something related to
    // asynchronation of javascript?.

}

function displayTasks() {
    // display all tasks currently stored in the web Storage API
    // clean all displayed tasks:

    removeDuplicates();
    removeEmptyTask();

    // return the sorted array of associative array, like:
    // [{111111111: "a"}, {111111113: "b"}]
    const sortedNestedArray = Object.keys(localStorage)
        .map(key => key)
        .sort() // alphabetic sort
        .map(key => ({[key]: localStorage[key] }))


    while (unordList.firstChild) {
        unordList.removeChild(unordList.firstChild);
      }

    // Populate tasks one by one
    if (localStorage.length === 0) {
        // pass
    } else {
        for (timeAndTask of sortedNestedArray) {

            const timestamp = Object.keys(timeAndTask)[0]
            const task = localStorage.getItem(timestamp)

            console.log(timestamp)

            const listItem = document.createElement("li");
            const span = document.createElement("span");
            const doneBtn = document.createElement("button")

            listItem.appendChild(span);
            listItem.appendChild(doneBtn);

            span.textContent = task;
            doneBtn.textContent = 'Done';
            unordList.appendChild(listItem);
            doneBtn.addEventListener("click", () => {
                localStorage.removeItem(timestamp)
                displayTasks();
            })

        }
    }
    console.log(localStorage);
}


// Without this function, somehow the localStorage.setItem in storeData()
// is executed multiple times, resulting in multiple entries
function removeDuplicates() {
    var entrySoFar = [];
    for (var i = 0; i < localStorage.length; i++) {
        // console.log(`key is ${i}`)
        // console.log(`entry so far is ${entrySoFar}`)
        // console.log(`localStorage.key(i) is ${localStorage.key(i)}`)
        if (entrySoFar.includes(localStorage.getItem(localStorage.key(i)))) {
            localStorage.removeItem(localStorage.key(i))
        } else {
            entrySoFar.push(localStorage.getItem(localStorage.key(i)))
        }
    }
}

// Without this function, somehow the localStorage.setItem in storeData()
// may be executed on empty form, resulting in empty entries
function removeEmptyTask() {
    for (var i = 0; i < localStorage.length; i++) {
        if (localStorage.getItem(localStorage.key(i)) === '') {
            localStorage.removeItem(localStorage.key(i))
        } 
    }
}

displayTasks()