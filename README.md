# dot-feed
Keeping track of how governments (usually called department of transportation) announce road construction projects.

## Why?

A large part of [OpenStreetMap](https://www.openstreetmap.org/)'s work is making sure existing data is kept up to date. One of the ways we can do this is to get notified of changes to the real world. Most governments propose and track these changes through their Department of Transportation (thus the name of this repository).

This repository is meant to track the methods these organizations announce their changes in an attempt to build a system that automatically tracks and notifies of upcoming changes to the road network.

## How?

For now, the goal should be to find each US state's DOT page and if it has a programmatic feed (e.g. RSS or e-mail) of some sort. We should also look for contact information for the DOT. Let's write [GitHub tickets](https://github.com/osmlab/dot-feed/issues/new) when new DOTs or feeds are found until we can decide on a format for the information.

Depending on the results of this survey, it might make sense to build some sort of conglomerated feed based on each DOT's individual feed. That feed could be filtered (so that only relevant changes are surfaced) and then shown on an RSS feed itself or on a website. Whatever's easiest for mappers to use.
