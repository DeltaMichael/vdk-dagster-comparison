# vdk-dagster-comparison

# Overview

This comparison looks at several examples of the same data job executed both in
dagster and vdk. After each example, logs from successful and failed runs for
both jobs are analyzed and compared on the basis of usability and readability.

# Data Jobs

## Hello Dagster

This data job fetches the top 10 hacker news stories ids, creates an adjaceny
list of child stories and stores various other metadata in a csv format. We run
it once successfully and look at the logs. We then break it, by pointing to a
non-existant json file in the second step and look at the logs again

### Successful run

#### Dagster

**Local logs**

On success

```
2023-07-27 17:25:52 +0300 - dagster - INFO - Using temporary directory /Users/mdilyan/Projects/vdk-dagster-comparison/dagster-hello-in-dagster/tmp4kcf6ogu for storage. This will be removed when dagster dev exits.
2023-07-27 17:25:52 +0300 - dagster - INFO - To persist information across sessions, set the environment variable DAGSTER_HOME to a directory to use.
2023-07-27 17:25:53 +0300 - dagster - INFO - Launching Dagster services...
2023-07-27 17:25:55 +0300 - dagster.daemon - INFO - Instance is configured with the following daemons: ['AssetDaemon', 'BackfillDaemon', 'SchedulerDaemon', 'SensorDaemon']
2023-07-27 17:25:55 +0300 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
2023-07-27 17:25:55 +0300 - dagster-webserver - INFO - Serving dagster-webserver on http://127.0.0.1:3000 in process 64030
2023-07-27 17:26:27 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64047 - RUN_START - Started execution of run for "__ASSET_JOB".
2023-07-27 17:26:27 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64047 - ENGINE_EVENT - Executing steps using multiprocess executor: parent process (pid: 64047)
2023-07-27 17:26:27 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64047 - hackernews_top_story_ids - STEP_WORKER_STARTING - Launching subprocess for "hackernews_top_story_ids".
2023-07-27 17:26:28 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64050 - STEP_WORKER_STARTED - Executing step "hackernews_top_story_ids" in subprocess.
2023-07-27 17:26:28 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64050 - hackernews_top_story_ids - RESOURCE_INIT_STARTED - Starting initialization of resources [io_manager].
2023-07-27 17:26:28 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64050 - hackernews_top_story_ids - RESOURCE_INIT_SUCCESS - Finished initialization of resources [io_manager].
2023-07-27 17:26:28 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64050 - LOGS_CAPTURED - Started capturing logs in process (pid: 64050).
2023-07-27 17:26:28 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64050 - hackernews_top_story_ids - STEP_START - Started execution of step "hackernews_top_story_ids".
2023-07-27 17:26:28 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64050 - hackernews_top_story_ids - STEP_OUTPUT - Yielded output "result" of type "Any". (Type check passed).
2023-07-27 17:26:28 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - hackernews_top_story_ids - Writing file at: /Users/mdilyan/Projects/vdk-dagster-comparison/dagster-hello-in-dagster/tmp4kcf6ogu/storage/hackernews_top_story_ids using PickledObjectFilesystemIOManager...
2023-07-27 17:26:29 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64050 - hackernews_top_story_ids - ASSET_MATERIALIZATION - Materialized value hackernews_top_story_ids.
2023-07-27 17:26:29 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64050 - hackernews_top_story_ids - HANDLED_OUTPUT - Handled output "result" using IO manager "io_manager"
2023-07-27 17:26:29 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64047 - hackernews_top_stories - STEP_WORKER_STARTING - Launching subprocess for "hackernews_top_stories".
2023-07-27 17:26:31 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64057 - STEP_WORKER_STARTED - Executing step "hackernews_top_stories" in subprocess.
2023-07-27 17:26:31 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64057 - hackernews_top_stories - RESOURCE_INIT_STARTED - Starting initialization of resources [io_manager].
2023-07-27 17:26:31 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64057 - hackernews_top_stories - RESOURCE_INIT_SUCCESS - Finished initialization of resources [io_manager].
2023-07-27 17:26:31 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64057 - LOGS_CAPTURED - Started capturing logs in process (pid: 64057).
2023-07-27 17:26:31 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64057 - hackernews_top_stories - STEP_START - Started execution of step "hackernews_top_stories".
2023-07-27 17:26:36 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64057 - hackernews_top_stories - STEP_OUTPUT - Yielded output "result" of type "Any". (Type check passed).
2023-07-27 17:26:36 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - hackernews_top_stories - Writing file at: /Users/mdilyan/Projects/vdk-dagster-comparison/dagster-hello-in-dagster/tmp4kcf6ogu/storage/hackernews_top_stories using PickledObjectFilesystemIOManager...
2023-07-27 17:26:36 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64057 - hackernews_top_stories - ASSET_MATERIALIZATION - Materialized value hackernews_top_stories.
2023-07-27 17:26:36 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64057 - hackernews_top_stories - HANDLED_OUTPUT - Handled output "result" using IO manager "io_manager"
2023-07-27 17:26:36 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64047 - ENGINE_EVENT - Multiprocess executor: parent process exiting after 9.38s (pid: 64047)
2023-07-27 17:26:36 +0300 - dagster - DEBUG - __ASSET_JOB - 8c1ead22-48ff-4690-9009-810552b925a3 - 64047 - RUN_SUCCESS - Finished execution of run for "__ASSET_JOB".
```

On failure

```
2023-07-27 17:17:02 +0300 - dagster - INFO - Using temporary directory /Users/mdilyan/Projects/vdk-dagster-comparison/dagster-hello-in-dagster/tmpz8s1rjmt for storage. This will be removed when dagster dev exits.
2023-07-27 17:17:02 +0300 - dagster - INFO - To persist information across sessions, set the environment variable DAGSTER_HOME to a directory to use.
2023-07-27 17:17:04 +0300 - dagster - INFO - Launching Dagster services...
2023-07-27 17:17:07 +0300 - dagster.daemon - INFO - Instance is configured with the following daemons: ['AssetDaemon', 'BackfillDaemon', 'SchedulerDaemon', 'SensorDaemon']
2023-07-27 17:17:08 +0300 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
2023-07-27 17:17:08 +0300 - dagster-webserver - INFO - Serving dagster-webserver on http://127.0.0.1:3000 in process 61735
2023-07-27 17:17:27 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61803 - RUN_START - Started execution of run for "__ASSET_JOB".
2023-07-27 17:17:27 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61803 - ENGINE_EVENT - Executing steps using multiprocess executor: parent process (pid: 61803)
2023-07-27 17:17:27 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61803 - hackernews_top_story_ids - STEP_WORKER_STARTING - Launching subprocess for "hackernews_top_story_ids".
2023-07-27 17:17:28 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61808 - STEP_WORKER_STARTED - Executing step "hackernews_top_story_ids" in subprocess.
2023-07-27 17:17:28 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61808 - hackernews_top_story_ids - RESOURCE_INIT_STARTED - Starting initialization of resources [io_manager].
2023-07-27 17:17:28 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61808 - hackernews_top_story_ids - RESOURCE_INIT_SUCCESS - Finished initialization of resources [io_manager].
2023-07-27 17:17:28 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61808 - LOGS_CAPTURED - Started capturing logs in process (pid: 61808).
2023-07-27 17:17:28 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61808 - hackernews_top_story_ids - STEP_START - Started execution of step "hackernews_top_story_ids".
2023-07-27 17:17:29 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61808 - hackernews_top_story_ids - STEP_OUTPUT - Yielded output "result" of type "Any". (Type check passed).
2023-07-27 17:17:29 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - hackernews_top_story_ids - Writing file at: /Users/mdilyan/Projects/vdk-dagster-comparison/dagster-hello-in-dagster/tmpz8s1rjmt/storage/hackernews_top_story_ids using PickledObjectFilesystemIOManager...
2023-07-27 17:17:29 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61808 - hackernews_top_story_ids - ASSET_MATERIALIZATION - Materialized value hackernews_top_story_ids.
2023-07-27 17:17:29 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61808 - hackernews_top_story_ids - HANDLED_OUTPUT - Handled output "result" using IO manager "io_manager"
2023-07-27 17:17:29 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61803 - hackernews_top_stories - STEP_WORKER_STARTING - Launching subprocess for "hackernews_top_stories".
2023-07-27 17:17:31 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61815 - STEP_WORKER_STARTED - Executing step "hackernews_top_stories" in subprocess.
2023-07-27 17:17:31 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61815 - hackernews_top_stories - RESOURCE_INIT_STARTED - Starting initialization of resources [io_manager].
2023-07-27 17:17:31 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61815 - hackernews_top_stories - RESOURCE_INIT_SUCCESS - Finished initialization of resources [io_manager].
2023-07-27 17:17:31 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61815 - LOGS_CAPTURED - Started capturing logs in process (pid: 61815).
2023-07-27 17:17:31 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61815 - hackernews_top_stories - STEP_START - Started execution of step "hackernews_top_stories".
2023-07-27 17:17:31 +0300 - dagster - DEBUG - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61803 - ENGINE_EVENT - Multiprocess executor: parent process exiting after 4.41s (pid: 61803)
2023-07-27 17:17:31 +0300 - dagster - ERROR - __ASSET_JOB - e353021e-8236-4121-a43f-749ff3bc5431 - 61803 - RUN_FAILURE - Execution of run for "__ASSET_JOB" failed. Steps failed: ['hackernews_top_stories'].
2023-07-27 17:18:08 +0300 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
```

**Browser logs**

On success

![img](images/dagster-success-1.png)
![img](images/dagster-success-2.png)
![img](images/dagster-success-3.png)
![img](images/dagster-success-4.png)
![img](images/dagster-success-5.png)
![img](images/dagster-success-6.png)

On error

![img](images/dagster-error-1.png)
![img](images/dagster-error-2.png)
![img](images/dagster-error-3.png)

#### VDK

**Local logs**

**Browser logs**
