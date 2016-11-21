mvn clean package
mv target/appserver-0.0.1-SNAPSHOT.jar target/appserver.jar
cp appserver.release.config target/appserver.config
cp config target/ -r
cp html target/ -r