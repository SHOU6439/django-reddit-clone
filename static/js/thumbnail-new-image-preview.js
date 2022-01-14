function previewThumbnailImage(obj)
{
	var fileReader = new FileReader();
	fileReader.onload = (function() {
		document.getElementById('preview_new_thumbnail').src = fileReader.result;
	});
	fileReader.readAsDataURL(obj.files[0]);
}