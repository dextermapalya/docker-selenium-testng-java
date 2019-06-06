package test.java;

import org.openqa.selenium.WebDriver;
//import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.phantomjs.PhantomJSDriver;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import java.net.MalformedURLException;

import java.net.URL;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.Platform;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.chrome.ChromeOptions;  //import ChromeOptions


public class SeleniumDockerGrid {

    private static WebDriver driver;

    @BeforeClass
    public static void openBrowser() throws MalformedURLException {
        DesiredCapabilities chromeCapabilities = DesiredCapabilities.chrome();
        final ChromeOptions chromeOptions = new ChromeOptions();
        //chromeOptions.setBinary("/usr/bin/chromium-browser");
        chromeOptions.addArguments("--headless");
        chromeCapabilities.setCapability(ChromeOptions.CAPABILITY, chromeOptions);

        chromeCapabilities.setBrowserName("chrome");



        //chromeCapabilities.setVersion("2.24");
        //String driverPath = System.getProperty("user.dir") + "/build/webdriver/chromedriver/chromedriver";
        //System.setProperty("webdriver.chrome.driver", driverPath);


        if(System.getProperty("webdriver.chrome.driver") != null)
            //driver = new ChromeDriver();
            
            //driver = new RemoteWebDriver(new URL("http://172.22.0.2:4444/wd/hub"), chromeCapabilities);
            driver = new RemoteWebDriver(new URL("http://selenium-hub:4444/wd/hub"), chromeCapabilities);
        else if(System.getProperty("phantomjs_binary_path") != null)
            driver = new PhantomJSDriver();
        else
            throw new RuntimeException("Unknown web driver specified.");

        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
    }

    @AfterClass
    public static void closeBrowser(){
        driver.quit();
    }

    @Test()
    public void browserInitTest() {
        driver.get("http://www.google.com/");
        Assert.assertEquals(driver.getTitle(),"Google");

    }
}
