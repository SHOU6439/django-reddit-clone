function previewHeaderImage(obj)
{
	var fileReader = new FileReader();
	fileReader.onload = (function() {
		document.getElementById('preview_new_header').src = fileReader.result;
	});
	fileReader.readAsDataURL(obj.files[0]);
}
