function addTask() {
    let taskInput = document.getElementById("taskInput");
    let taskText = taskInput.value.trim(); // trim removes ends from left and right side
    if (taskText === "") {
        alert("Please enter a task!");
        return;
    }
    let taskList = document.getElementById("taskList");
    let li = document.createElement("li");
    let span = document.createElement("span");
    span.textContent = taskText;
    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.addEventListener("change", function () {
        li.classList.toggle("completed", checkbox.checked);
    });

    let deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.className = "delete-btn";
    deleteBtn.onclick = function () {
        taskList.removeChild(li);
    };

    li.appendChild(span);
    li.appendChild(checkbox);
    li.appendChild(deleteBtn);
    taskList.appendChild(li);

    taskInput.value = "";
}
