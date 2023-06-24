const unordList = document.querySelector("ul");
const input = document.querySelector("input");
const addBtn = document.querySelector("#add");
const clearAllBtn = document.querySelector("#clear-all")

addBtn.addEventListener("click", () => {

    const currText = input.value
    storeData(currText);
    input.value = '';
    displayTasks();
  
})

clearAllBtn.addEventListener("click", () => {
    const currStorageLength = localStorage.length
    // clean all displayed tasks:
    while (unordList.firstChild) {
        unordList.removeChild(unordList.firstChild);
      }
    // remove all tasks in localStorage
    for (var i = 0; i < currStorageLength; i++) {
        localStorage.removeItem(localStorage.key(0));
    }

})

function storeData(currText) {
    // store a task written on the form

    // const currStorageLength = localStorage.length
    console.log(`storing data... localStorage.length = ${localStorage.length}`)

    localStorage[`${currText}`] = currText
    // Note about this code:
    // Due to unknown reason, this line 34 seems to be very buggy.
    // 
    // Other localStorage[`${localStorage.length}`] = currText or
    // localStorage.setItem(localStorage.length) = currText will be executed multiple times and
    // thus are not appropriate here.
    // Since the console.log above is executed only once, storeData triggering seems to be fine.
    // I am not sure if it is a problem of the localStorage.setItem or something related to
    // asynchronation of javascript?.
    

}

function displayTasks() {
    // display all tasks currently stored in the web Storage API
    // clean all displayed tasks:
    while (unordList.firstChild) {
        unordList.removeChild(unordList.firstChild);
      }

    // read localStorage.length
    // then populate for it one by one
    if (localStorage.length === 0) {
        // pass
    } else {
        for (var i = 0; i < localStorage.length; i++) {
            const id = localStorage.key(i)
            const task = localStorage.getItem(`${id}`)
            
            console.log(id)

            const listItem = document.createElement("li");
            const span = document.createElement("span");
            const doneBtn = document.createElement("button")

            listItem.appendChild(span);
            listItem.appendChild(doneBtn);

            span.textContent = task;
            doneBtn.textContent = 'Done';
            unordList.appendChild(listItem);
            doneBtn.addEventListener("click", (e) => {
                localStorage.removeItem(id)
                e.parentNode.remove();
                displayTasks();
            })

        }
    }
    console.log(localStorage);

    // pass
}

displayTasks()