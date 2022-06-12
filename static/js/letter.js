$(document).ready(function () {
    show_comment();
});

function show_comment() {
    $('#comment-list').empty();
    $.ajax({
        type: 'GET',
        url: '/happy',
        data: {},
        success: function (response) {
            let rows = response['friend']
            for (let i = 0; i < rows.length; i++) {
                let name = rows[i]['name']
                let comment = rows[i]['comment']
                let num  = rows[i]['num']

                console.log(rows[i])
                let temp_html = `<div class="card">
                                    <div class="card-body">
                                        <blockquote class="blockquote mb-0">
                                            <p>${comment}
                                                <button type="button" class="btn_delete" onclick="delete_message(${num})">삭제</button>
                                            </p>
                                            <footer class="blockquote-footer">${name}</footer>
                                        </blockquote>
                                    </div>
                                </div>`

                $('#comment-list').append(temp_html);
            }
        }
    });
}

function save_comment() {
    let name = $('#name').val()
    let comment = $('#comment').val()

    $.ajax({
        type: "POST",
        url: "/happy",
        data: {name_give: name, comment_give: comment},
        success: function (response) {
            alert(response['msg'])
            window.location.reload()
        }
    })
}

function delete_message(num){
    $.ajax({
        type: "POST",
        url: "/message/done",
        data: {message_give:num},
        success: function (response) {
            alert(response["msg"])
            window.location.reload()
        }
    });
}
