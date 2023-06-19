echo update openapi-generator
./bin/utils/openapi-generator-cli.sh
rm -Rf ./namsor/client/python/*
echo run openapi-generator
java -jar modules/openapi-generator-cli/target/openapi-generator-cli.jar generate  --git-repo-id namsor-python-sdk2 --git-user-id namsor --skip-validate-spec -i https://v2.namsor.com/NamSorAPIv2/api2/openapi.json -g python -o  namsor/client/python  --additional-properties packageVersion=2.0.26
#~/dropbox_uploader.sh upload namsor-sdk2-1.0.0.jar namsor-sdk2-1.0.0.jar
#~/dropbox_uploader.sh upload namsor-sdk2-1.0.0-javadoc.jar namsor-sdk2-1.0.0-javadoc.jar
#~/dropbox_uploader.sh upload namsor-sdk2-1.0.0-sources.jar namsor-sdk2-1.0.0-sources.jar
#~/dropbox_uploader.sh upload namsor-sdk2-1.0.0-tests.jar namsor-sdk2-1.0.0-tests.jar
cp -R /home/namsor/codegen/openapi-generator/namsor/client/python/* /home/namsor/codegen/namsor-python-sdk2/
cp /home/namsor/codegen/openapi-generator/run-python.bash /home/namsor/codegen/namsor-python-sdk2/

