FROM adoptopenjdk/openjdk11:ubi
MAINTAINER da.ajou.ac.kr
COPY gradlew .
COPY gradle gradle
COPY build.gradle .
COPY settings.gradle .
COPY src src
RUN chmod +x ./gradlew
RUN ./gradlew clean
RUN ./gradlew bootRun

ENTRYPOINT ["./gradlew","bootRun"]

# 나중에 수정할 점 : gradle 다운로드하는데 너무 오래 걸림, github action에서 build해서 .jar만 올리기

# RUN ./gradlew bootJar

# ARG JAR_FILE=build/libs/*.jar
# COPY ${JAR_FILE} app.jar
# ENTRYPOINT ["java","-jar","/app.jar"]