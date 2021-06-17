
$(function() {
    $("#dataTable tbody td").click(function (event) {
        var pk = $(this).closest("tr").children("td").first().text();
        console.log("table row clicked"+pk)  // sanity check
        update_details(pk);
        return false;
    });

    function update_details(pk) {
        console.log("update details is called")

        $.ajax({
            // the GET must also receive the PK of the DB object corresponding to the row clicked.
            // this.parentElement.parentElement.getElementsByTagName("td")[0].getElementsByTagName("a")[0].innerHTML
            // var pk = this.parentElement.parentElement.getElementsByTagName("td")[0].getElementsByTagName("a")[0].innerHTML;

            // must include the app endpoint at the beginning, others it appends to current url, e.. ajaxlist/get_ajax_details/
            url: "/myapp/get_ajax_details/",
            type: "GET",
            data: {"pk":pk},

            // success
            success: function (rendered_template) {
                $('#details').empty();
                $('#details').prepend(rendered_template)
                console.log(rendered_template);
                console.log("success")
            },

            // error
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }

        });
    };

});