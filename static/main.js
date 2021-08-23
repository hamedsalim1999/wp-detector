function download(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);
  
    element.style.display = 'none';
    document.body.appendChild(element);
  
    element.click();
  
    document.body.removeChild(element);
  }

$('#process-file-button').on('click', function (e) {
    let files = new FormData(), // you can consider this as 'data bag'
        url = '/uploadFiles';

    files.append('file', $('#file')[0].files[0]); // append selected file to the bag named 'file'

    $.ajax({
        type: 'post',
        url: url,
        processData: false,
        contentType: false,
        data: files,
        success: function (response) {
            download('test.csv',response);
        },
        error: function (err) {
            console.log(err);
        }
    });
});