## How to run selenium test using gradle testng


#### Install JAVA (any provider, openjdk or oracle java)

#### Clone the project from
          $ git clone https://github.com/dexterm/testng-selenium-gradle-chrome-firefox.git

If you wish to run gradle from any folder then export PATH environment variable

          $ export PATH=$PATH:/opt/gradle/gradle-4.10.2/bin

Change the gradle path to match the folder in your system
Optionally you can add the path to .bashrc

1. Open the `.bashrc` file in your home directory (for example, `/home/your-user-name/.bashrc`) in a text editor.
2. Add `export PATH=$PATH:/opt/gradle/gradle-4.10.2/bin` to the last line of the file, where *your-dir* is the directory you want to add.
3. Save the `.bashrc` file.
4. Restart your terminal.

#### Launch a test using chrome browser
          $ ./gradlew testChrome

#### Launch a headless test using phantomJS
          $ ./gradlew testPhantomJs

## Notes

When running from Gradle -- the build script will automatically try to download required OS specific drivers for Chrome or PhatomJS, and update requirement environment variables -- phantomjs.binary.path or webdriver.chrome.driver

When running from an IDE -- you will need these environment variables setup and pointing to the correct webdriver

Example for running individual tests from the commandline: gradle testPhantomJs -Dtest.single=TestNgExample


### How to run the test using docker
[How to run the test using docker](docs/how_to_run_test_using_docker.md)
