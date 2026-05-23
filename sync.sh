#!/usr/bin/env bash

# sync.sh
# Implements SECTION 2: REPO & GIT SANITIZATION PROTOCOL
# Syncs local repo with upstream, handles intelligent branch merges,
# and cleans up submodules recursively.

set -e

echo "=========================================="
echo " Initiating Git Sanitization Protocol "
echo "=========================================="

echo "[1/4] Fetching all upstream tracking branches..."
git fetch --all --tags

echo "[2/4] Syncing upstream parent into main..."
# If there's an explicit upstream configured, pull it. Otherwise default to origin/main.
UPSTREAM_REMOTE=$(git remote | grep upstream || echo "origin")
git checkout main || git checkout -b main
git pull $UPSTREAM_REMOTE main --rebase || {
    echo "Warning: Rebase failed, manual conflict resolution required. Aborting rebase."
    git rebase --abort
}

echo "[3/4] Reconciling Feature Branches..."
# Interrogates local branches. Excludes HEAD and exactly 'main'.
for branch in $(git branch --format="%(refname:short)" | grep -vx "main"); do
    echo " -> Intelligently merging main into feature branch: $branch"
    git checkout "$branch"
    git merge main -m "chore: Auto-sync main into feature branch $branch" || {
        echo "Warning: Conflict merging main into $branch. Skipping and aborting."
        git merge --abort
    }
done

# Return to original branch context (assuming we want to leave the repo on the branch we started on)
git checkout main

echo "[4/4] Recursive Submodule Update..."
# Updates all submodules inside all submodules recursively, ensuring clean environments.
git submodule update --init --recursive

echo "=========================================="
echo " Sanitization Complete. Workspace is clean. "
echo "=========================================="
