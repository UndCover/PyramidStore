
## Pyramid添加教程

以下代码使用TVBOXOSC最后一个版本作为样例，其他的衍生版本请自行参考。目前只支持armeabi-v7a和x86_64，测试结束后续会放出所有版本支持

### 添加过程

##### 1.添加pyramid.aar到android项目libs目录下

##### 2.在 app\build.gradle 中添加内容
```gralde
dependencies {
    //添加pyramid.aar引用
    implementation files('libs\\pyramid.aar')
}
```
##### 3.在 app\proguard-rules.pro 中添加内容
```pro
-keep public class com.undcover.freedom.pyramid.** { *; }
-dontwarn com.undcover.freedom.pyramid.**
-keep public class com.chaquo.python.** { *; }
-dontwarn com.chaquo.python.**
```
##### 4.修改项目 App.java
```java
// 添加引用
import com.undcover.freedom.pyramid.PythonLoader;

public class App extends MultiDexApplication {
    //...
}
```
```java
public void onCreate() {
	// ....
	PlayerHelper.init();
    //pyramid-add-start
	PythonLoader.getInstance().setApplication(this);
    //pyramid-add-end
}
```
##### 5.修改 ApiConfig.java
```java
// 添加引用
import com.github.catvod.crawler.SpiderNull;
import com.undcover.freedom.pyramid.PythonLoader;
public class ApiConfig {
    //...
}
```

```java
private void parseJson(String apiUrl, String jsonStr) {
    //pyramid-add-start
	PythonLoader.getInstance().setConfig(jsonStr);
    //pyramid-add-end
	JsonObject infoJson = new Gson().fromJson(jsonStr, JsonObject.class);
	//....
}
```

```java
public Spider getCSP(SourceBean sourceBean) {
    //pyramid-add-start
    if (sourceBean.getApi().startsWith("py_")) {
        try {
            return PythonLoader.getInstance().getSpider(sourceBean.getKey(), sourceBean.getExt());
        } catch (Exception e) {
            e.printStackTrace();
            return new SpiderNull();
        }
    }
    //pyramid-add-end
    return jarLoader.getSpider(sourceBean.getKey(), sourceBean.getApi(), sourceBean.getExt());
}
```

```java
public Object[] proxyLocal(Map param) {
    //pyramid-add-start
    try {
        if(param.containsKey("api")){
            String doStr = param.get("do").toString();
            if(doStr.equals("ck"))
                return PythonLoader.getInstance().proxyLocal("","",param);
            SourceBean sourceBean = ApiConfig.get().getSource(doStr);
            return PythonLoader.getInstance().proxyLocal(sourceBean.getKey(),sourceBean.getExt(),param);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    //pyramid-add-end
    return jarLoader.proxyInvoke(param);
}
```