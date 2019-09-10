// import the serious stuff
#include<stdio.h>
#include<curl/curl.h>


// the main function
int main()
{
	// global init stuff
	curl_global_init(CURL_GLOBAL_ALL);

	// curl handle
	CURL *curl_handle;
	CURLcode result;

	// initialize the easy interface
	curl_handle = curl_easy_init();

	// fetch a page

	// return nothing
	return 0;
}
