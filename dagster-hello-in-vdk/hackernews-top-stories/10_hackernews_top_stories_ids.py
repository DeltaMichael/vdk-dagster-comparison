# Copyright 2021-2023 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0

import logging
import json
import pandas as pd
import requests

from vdk.api.job_input import IJobInput

log = logging.getLogger(__name__)


def run(job_input: IJobInput):
    """Get top stories from the HackerNews top stories endpoint.

    API Docs: https://github.com/HackerNews/API#new-top-and-best-stories.
    """
    top_story_ids = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json"
    ).json()

    with open("hackernews_top_story_ids.json", "w") as f:
        json.dump(top_story_ids[:10], f)


