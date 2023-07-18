let rootUrl = "http://127.0.0.1:8000/";
const unordList = document.querySelector("ul");
const input = document.querySelector("input");
const addBtn = document.querySelector("#add");
// const clearAllBtn = document.querySelector("#clear-all")
const errorText = document.querySelector('#error-text')

let userkey = ""
let errorType = ""


addBtn.addEventListener("click", () => {
    errorText.textContent = "";
    errorText.className = "";
    const currText = input.value
    if (validateInput()) {
        createData(url = baseUrl, data = {"title":`${currText}`})
            .then(data => {
                showCreatedData(data);
            })
            .catch(error => {
                console.error(`Could not add a task: ${error}`)
            });
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


// clearAllBtn.addEventListener("click", () => {
//     const currStorageLength = localStorage.length
//     // clean all displayed tasks:
//     clearAllDisplayedTasks();
//     // remove all tasks in localStorage
//     clearAllData(url = baseUrl)
//         .then(console.log(`All tasks successfully deleted`))
// })

// async function clearAllData(url = baseUrl)  {
//     const response = await fetch(url, {
//       method: 'DELETE', 
//       headers: {
//         'Content-Type': 'application/json'
//       }
//     });
//     return response.json(); 
//   }

async function createData(url = baseUrl, data = {"title":`buy clothing`}) {
    const response = await fetch(url, {
      method: 'POST', 
      headers: {
        'Content-Type': 'application/json'
        // 'Authorization': 'Bearer your-token' (if needed)
      },
      body: JSON.stringify(data) 
    });
    return response.json(); 
  }
  


async function listTasks(url = baseUrl) {
    const response = await fetch(url, {
      method: 'GET', 
      headers: {
        'Content-Type': 'application/json',
        // 'Authorization': 'Bearer your-token' (if needed)
      }
    });
    return await response.json();
}


async function deleteTask(baseUrl = baseUrl, taskId) {
    const response = await fetch(url = `${baseUrl}/${taskId}`, {
      method: 'DELETE', 
      headers: {
        'Content-Type': 'application/json'
        // 'Authorization': 'Bearer your-token' (if needed)
      }
    });
    return response.json(); 
  }


// below are code for changing display

function showCreatedData(task = data) {
    const listItem = document.createElement("div");
    const span = document.createElement("span");
    const doneBtn = document.createElement("button");
    listItem.classList.add("flex", "flex-row", "w-full");
    doneBtn.classList.add("p-0", "m-1", "border-2", "border-teal-300", "text-teal-600", "rounded", "justify-self-end", "w-12");
    doneBtn.classList.add("hover:text-white", "hover:bg-teal-400", "active:bg-teal-600", "focus:ring", "focus:ring-teal-300");
    span.classList.add("flex-grow", "m-1");
    listItem.appendChild(span);
    listItem.appendChild(doneBtn);
    span.textContent = task.title;
    doneBtn.textContent = 'Done';
    unordList.appendChild(listItem);
    doneBtn.addEventListener("click", () => {
        deleteTask(baseUrl, task.id)
            .then(console.log(`ID ${task.id} : \"${task.title}\" was successfully deleted`))
            .then(listItem.remove())
            .catch(error => {
                console.error(`Could not delete a task of ${task.id} : ${task.title} - ${error}`)
            })
    })
    console.log(`ID ${task.id} : \"${task.title}\" was successfully added`)
}

function clearAllDisplayedTasks() {
    while (unordList.firstChild) {
        unordList.removeChild(unordList.firstChild);
    }
}

function displayTasks() {
    // display all tasks currently stored in the web Storage API
    // clean all displayed tasks:
    
    clearAllDisplayedTasks()

    // removeDuplicates();
    // removeEmptyTask();
    listTasks()
        .then((tasks) => {
            console.log(tasks)
            if (tasks.length != 0) {
                for (const task of tasks) {
                    showCreatedData(task);
                }
            }
        })

}

function initializeDisplay() {
    if (localStorage.getItem("userkey") === null) {
        localStorage.setItem("userkey", makeUserKey(16))
        userkey = localStorage.getItem("userkey")
        createUser(userkey)
            .then((response) => {
                console.log(console.log(`${response.url}: ${response.status}`))
            })
            .catch((error) => {
                console.error(`Failed to fetch: ${error}`);
              });
    }
    userkey = localStorage.getItem("userkey")
    baseUrl = rootUrl + `users/${userkey}/tasks`
    displayTasks()
    
}

async function createUser(userkey) {
    createUrl = rootUrl + `users`
    const response = await fetch(createUrl, {
        method: 'POST', 
        headers: {
          'Content-Type': 'application/json',
          "user_key": userkey
          // 'Authorization': 'Bearer your-token' (if needed)
        },
        body: JSON.stringify(data) 
      });
      return response.json(); 
}


function makeUserKey(length) {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    let counter = 0;
    while (counter < length) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
      counter += 1;
    }
    return result;
}

initializeDisplay()