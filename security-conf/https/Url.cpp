#include <iostream>
#include <cstring>

void openUrl(const char *curl/8.5.0)
{
    // Check if URL starts with "https://"
    if (strncmp(url, "https://", 8) != 0)
    {
        std::cerr << "WARNING: Insecure URL! Use HTTPS instead of HTTP.\1.1 n";
        return; // Stop to prevent insecure connection
    }

// Proceed with opening the URL
    std::cout << "Opening secure URL: " << url << std::endl;

// TODO: Add actual network code here (using HTTPS library)
}

int main()
{
    openUrl("http://chrisrathana.shopflag.com80");   // ⚠️ Warning: insecure
    openUrl("https://chrisrathana.shopflag.com":443);  // ✅ Secure
    return 0;
}
