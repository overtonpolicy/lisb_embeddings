# Matching abstracts to arbitray text

This is sample code from a presentation at the LIS-B 2024 conference in Brighton where we talked about how embeddings in a bibliometrics context are easy and cheap to explore.

It creates embeddings for a set of abstracts, stored in a text file one per line, and a set of Areas of Research Interest from the UK government, also stored in a text file one per line. It then compares the two to try and pair abstract / ARI pairs on the same subject.

There's some sample data in the repo to make this easier:

*abstracts.txt* - is the abstracts data, fetched from OpenAlex

*aris.txt* - is the aris data, fetched from the ari.org.uk API

## Seting up your environment

You'll need python3 installed.

Additionally on my machine I had to install the openai and scipy libraries:

        pip3 install openai
        pip3 install scipy

You may need to install the numpy library too in the same way.

## Creating embeddings

The `get_embeddings.py` script will read in a text file called `input.txt` and then save embeddings to a file called `embeddings.json`

It uses the OpenAI API, for which you'll need an API key - see https://platform.openai.com/signup

Edit the script to put your API key where it says xxx on this line:

        openai.api_key = "xxx"

If you want to use the sample files included in the repository, either edit the file to read `abstracts.txt` or `aris.txt`, or just copy one of them to a new file called `input.txt`

to run it, just do:

`python3 get_embeddings.py`

this took five minutes and cost < $0.1 on my macbook.

When the script has run you'll have a file called `embeddings.json`

## Comparing embeddings

The compare_embeddings.py script reads two sets of embeddings (in the format saved by `get_embeddings`, above) and then does pairwise comparisons between them.

It'll print out any pairs where the semantic distance is less than some arbitrary threshold (I used 0.45).

To use it with the data in this repo, run `get_embeddings.py` over the aris and abstracts and save the output to `ari_embeddings.json` and `paper_embeddings.json` respectively.

## Notes and caveats

This is very rough and ready, and just to show you how easy it is to get started. There's a lot to explore beyond this!

Cleaning your input data is usually more work than the actual analysis. We spent a lot of time cleaning up abstracts, policy documents and engagement opportunties like the ARIs (the two text files in this repository aren't cleaned, they're just raw outputs).

The model you use to create the embeddings can make a big difference - in this code we're using an off the shelf OpenAI model called `text-embedding-3-small`, but you'll hear about "fine tuned" models: these are models that somebody has reinforced certain relationships between words via lots of extra training data. You might want to, for example, find a model that has been fine tuned on scholarly content.


