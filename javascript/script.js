function validateForm()
{	
	if(document.forms["test_form"]["username"].value == "")
	{
		alert("This won't work");
		return false;
	}
	
	if(isNaN(document.forms["test_form"]["username"].value))
	{
		alert("This is a string");
		return false;
	}	
}
