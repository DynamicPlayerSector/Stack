function tick(checkbox)
{
    var data = {id: checkbox.parentNode.id, activated: checkbox.checked}
    fetch('/tick', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => {
        console.log(response)
    });
}

function archive(task)
{
    task.parentNode.remove();
    var data = {id: task.parentNode.id}
    fetch('/archive', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => {
        console.log(response)
    });
}