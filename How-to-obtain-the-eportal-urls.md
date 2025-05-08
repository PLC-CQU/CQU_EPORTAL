# How to obtain the eportal login and logout urls

We are trying to obtain the login and logout urls of the eportal of Chongquing University (Huxi campus).

The web url of the eportal is [http://10.254.7.4/](http://10.254.7.4/)

## How to obtain the eportal login url
* visit the eportal login page at http://10.254.7.4/a79.htm
![eportal login page](.images/eportal_login_page.png)


* input your username and password in the form fields on the right side
* before clicking the login button, right click your mouse and inspect the source code underline the login button
![eportal login inspection](.images/login_inspection.png)
* one can see that `javascript:ee(1)` is invoked when clicking the login button. find the function from the javascrpt files, which is in `a40.js`
![eportal login entry function](.images/login_entry_function.png)
* start debuging and clicking the login button and you will find the full login urls in `script.src`
![eportal login url](.images/login_urls.png)

## How to obtain the eportal logout url
You can obtain the eportal logout url similarly.

* visit the eportal page. Since you have already logged in, you will see the following page:
![eportal logout page](.images/eportal_logout_page.png)
* inspect the souce underlying the `logout` button and find the logout entry function `javascript:wc()`:
![eportal logout inspection](.images/logout_inspection.png)
* the entry function is also in `a40.js`, start debugging and clicking the logout button, you will find the full logout urls in `script.src`
![eportal logout url](.images/logout_urls.png) 



*Note*, I use Google Chrome above.