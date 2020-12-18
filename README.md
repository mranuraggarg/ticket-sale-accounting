# Ticket sale accounting

## Introduction
I have been part of the planetarium community since 1999. Later in 2006 I joined Nehru Planetarium, Delhi, India as a Planetarium Educator, and my relation with the planetarium grew even stronger. Although I left that post in 2009 for my further studies, but it is still my second home. In 2013, planetarium accountant came up with an idea that there should be a better way to calculate the daily OCCUPANCY STATEMENT, as he use to struggle a lot with it due to digital divide. Listening to his complains I started with this project. 

## About the software
This is my first ever graphical project, and since I was using Linux full time, I choose GTK+3 as my graphic toolkit. Although I was using Fortran at that time, but I wanted to explore Python more, and hence used that on the backend.

### Minimum Requrirements
We would be using Python 3.0. Based on this choice the minimum requrement would be:
- Python 3.0 or higher (I have recently checked this code on Python 3.9)
- GTK+3.0
- GTK+3.0 python binding, PyGObject3

#### Installing on Windows:
##### Let us start with Python 3

Follow these steps to download the full installer:

1. Open a browser window and navigate to the Python.org Downloads page for Windows.

2. Under the “Python Releases for Windows” heading, click the link for the Latest Python 3 Release - Python 3.x.x. As of this writing, the latest version was Python 3.9.0.

3. Scroll to the bottom and select either Windows x86-64 executable installer for 64-bit or Windows x86 executable installer for 32-bit.

4. Then follow the onscreen instructions

#### Installing on MacOS:
I would suggest to use the HomeBrew to install the dependencies. Use will see that install GTK+3.0 and its Python dependency is eaier to install through HomeBrew.

##### Let us start with Python 3

Follow these steps:

1. Before we install HomeBrew, we will need the command line tools for MacOS.
<code> xcode-select --install <code>
  
2. Copy paste the following code into the terminal:
<code> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" <code>

3. Now we will use the HomeBrew to *brew* the Python and other required packages. Excute
<code>brew install pygobject3 gtk+3 <code> in the terminal. it will install all the required dependencies, including Python 3.9.0
  
For more detailed instaruction head to https://pygobject.readthedocs.io/en/latest/getting_started.html


## Working
It was supposed to be a simple accounting software to calculate the total daily sale for Planetarium, as it was intended to be use by a person with limited computer based capabilities. So, I kept the layout as simple and as close to Excel as possible. It do only two primary tasks:
- Calculate the total sale
- Save the results as a HTML file.

## Conclusion
Being my first ever graphic based project and I was extremely new in Python, I would consider it to be pretty good. It does the intended task easily and it is extremely easy to port between Linux, Windows and MacOS.

Said that, it is still in its extremely crude form, as I never updated it after its initial deployment. Still, few of the upgrades I would like to work on are:
- Bifurcatint the code into functions.
- Saving data to SQL (or any-other database)
- Saving result in a PDF rather then HTML, for better porting.
- Taking direct print from the software.

These are just the few which I would like to start with and then see where it goes.
