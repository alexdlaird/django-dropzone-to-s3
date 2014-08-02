// Get the template HTML and remove it from the doumenthe template HTML and remove it from the doument
var previewNode = document.querySelector("#template");
previewNode.id = "";
var previewTemplate = previewNode.parentNode.innerHTML;
previewNode.parentNode.removeChild(previewNode);

var myDropzone = new Dropzone(document.body, { // Make the whole body a dropzone
    url: "/upload", // Set the url
    thumbnailWidth: 80,
    thumbnailHeight: 80,
    parallelUploads: 20,
    previewTemplate: previewTemplate,
    autoQueue: false, // Make sure the files aren't queued until manually added
    previewsContainer: "#previews", // Define the container to display the previews
    clickable: ".fileinput-button" // Define the element that should be used as click trigger to select files.
});

myDropzone.on("addedfile", function (file) {
    // Hookup the start button
    file.previewElement.querySelector(".start").onclick = function () {
        // Ensure the file is of a valid extension
        myDropzone.enqueueFile(file);
    };
});

// Update the total progress bar
myDropzone.on("totaluploadprogress", function (progress) {
    document.querySelector("#total-progress .progress-bar").style.width = progress + "%";
});

myDropzone.on("sending", function (file, xhr, formData) {
    // Show the total progress bar when upload starts
    document.querySelector("#total-progress").style.opacity = "1";
    // And disable the start button
    file.previewElement.querySelector(".start").setAttribute("disabled", "disabled");
    formData.append("csrfmiddlewaretoken", $('input[name="csrfmiddlewaretoken"]').val());
    if (document.shared_key) {
        formData.append("shared_key", document.shared_key);
    }
});

// Hide the total progress bar when nothing's uploading anymore
myDropzone.on("queuecomplete", function (progress) {
    document.querySelector("#total-progress").style.opacity = "0";
});

// Setup the buttons for all transfers
// The "add files" button doesn't need to be setup because the config
// `clickable` has already been specified.
document.querySelector("#actions .start").onclick = function () {
    myDropzone.enqueueFiles(myDropzone.getFilesWithStatus(Dropzone.ADDED));
};
document.querySelector("#actions .cancel").onclick = function () {
    myDropzone.removeAllFiles(true);
};

$(document).ready(function () {
    // Once the page is loaded, we need to poll the server for settings
    $.when($.ajax({
        type: 'GET',
        url: '/get_settings'
    })).then(function (data) {
        json = $.parseJSON(data);
        myDropzone.options.acceptedFiles = json.ALLOWED_FILE_MIME_TYPES.join();
        document.annonymousUploads = json.ANNONYMOUS_UPLOADS;

        // If annonymous uploads are not allowed, prompt the user for the shared key
        if (!json.ANNONYMOUS_UPLOADS) {
            document.shared_key = prompt("Enter the shared key to upload to this server:\n(If you do not have the shared key, contact " + json.CONTACT_EMAIL + ")");

            $.when($.ajax({
                data: {'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(), 'shared_key': document.shared_key},
                statusCode: {
                    400: function () {
                        // If we get a BadResponse, our shared key was incorrect, so reload the page to reprompt
                        location.reload();
                    }
                },
                type: 'POST',
                url: '/check_shared_key'
            })).then(function (data) {
                // If we get a clean response, the shared key was correct, so show the form
                $("#container").slideDown("fast");
            });
        }
        else {
            // If annonymous uploads are allowed
            $("#container").slideDown("fast");
        }
    });
});