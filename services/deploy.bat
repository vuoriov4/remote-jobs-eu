call az group create -l northeurope -n remote-jobs-eu-resource-group
call az storage account create --name remotejobseustorage --sku Standard_LRS --resource-group remote-jobs-eu-resource-group
call az storage table create --name jobs --account-name remotejobseustorage
call az storage table create --name tags --account-name remotejobseustorage
call az functionapp create --consumption-plan-location northeurope --runtime python --runtime-version 3.9 --functions-version 4 --name remote-jobs-eu-fnapp --os-type linux --storage-account remotejobseustorage --resource-group remote-jobs-eu-resource-group
call cd az-function
call cd api
call func azure functionapp publish remote-jobs-eu-fnapp
call az functionapp cors add -g remote-jobs-eu-resource-group -n remote-jobs-eu-fnapp --allowed-origins http://localhost:8080
call cd ..
call cd ..