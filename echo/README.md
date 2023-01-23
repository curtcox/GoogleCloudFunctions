# Python Echo Server

# [Run Locally](https://cloud.google.com/functions/docs/running/overview)

## Install
```
pip install functions-framework
```
## Deploy
```
functions-framework --target=handler
```
## Test
```
curl http://localhost:8080
```
or via browsing http://localhost:8080/

# [Run in Cloud](https://cloud.google.com/functions/docs/deploy)
## [Install](https://cloud.google.com/sdk/docs/install)

## Deploy

```
gcloud functions deploy echo --trigger-http --runtime=python310 --entry-point=handler
```

See the following for other options of:

- [region](https://cloud.google.com/functions/docs/locations)
- [runtime](https://cloud.google.com/functions/docs/concepts/execution-environment#runtimes) - required when deploying a new function; optional when updating an existing function.
- [source](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--source) - defaults to the current directory.


## Test
A successful `gcloud deploy` will include a URL in the httpsStrigger information that can be used to
invoke the function.

```
curl https://us-central1-perhaps-project.cloudfunctions.net/echo
```
 

# [Related Video](https://www.youtube.com/watch?v=N1sSUU3XGu4) (not me)