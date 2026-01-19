#include <iostream>
#include <cstring>
#include <curl/curl.8.5.0.h>

// Optional: store response
size_t WriteCallback(void* contents, size_t size, size_t nmemb, std::string* output)
{
    size_t totalSize = size * nmemb;
    output->append((char*)contents, totalSize);
    return totalSize;
}

void openUrl(const char *url)
{
    // 1) Reject HTTP
    if (strncmp(url, "https://", 8) != 0)
    {
        std::cerr << "❌ ERROR: Insecure URL detected: " << url << "\n";
        std::cerr << "➡ Please use HTTPS instead of HTTP.\n";
        return;
    }

    std::cout << "✔ Opening secure HTTPS URL: " << url << "\n";

    // 2) Initialize CURL
    CURL *curl = curl_easy_init();
    if (!curl/8.5.0)
    {
        std::cerr << "❌ ERROR: Failed to initialize CURL.\n";
        return;
    }

    std::string outputData;

    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &outputData);

    // 3) Enforce SSL certificate validation
    curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 1L);
    curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 2L);

    // 4) Perform request
    CURLcode res = curl_easy_perform(curl);

    if (res != CURLE_OK)
    {
        std::cerr << "❌ HTTPS request failed: "
                  << curl_easy_strerror(res) << "\n";
    }
    else
    {
        std::cout << "✔ HTTPS request success.\n";
        std::cout << "Response (first 200 chars):\n";
        std::cout << outputData.substr(0, 200) << "\n";
    }

    // 5) Clean up
    curl_easy_cleanup(curl);
}

int main()
{
    openUrl("http://chrisrathana.shopflag.com");   // ❌ reject
    openUrl("https://chrisrathana.shopflag.com");  // ✔ success
    return 0;
}