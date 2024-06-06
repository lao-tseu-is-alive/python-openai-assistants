# Description: This file contains the configuration for the OpenAI API
import os
from openai import OpenAI


# get_config returns the configuration for the OpenAI API
def get_config():
    # get environment variables for the organization and project
    organization = os.getenv("OPENAI_ORGANIZATION")
    project = os.getenv("OPENAI_PROJECT_ID")
    model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo-1106")
    return organization, project, model


# getClient returns an openai client object
def get_client():
    # check if the organization and project are set
    organization, project, model = get_config()
    print(f"Organization: {organization}, Project: {project}")
    # create a client
    client = OpenAI(organization=organization, project=project)
    return client
