# Binder Configuration Files

This directory contains configuration files for optimizing MyBinder.org builds.

## Files:

- **environment.yml**: Conda environment specification (primary config)
- **runtime.txt**: Python version specification
- **postBuild**: Post-installation script for cleanup and optimization

## Optimization Strategy:

1. **Conda over pip**: Faster dependency resolution
2. **Minimal packages**: Only essential packages, no version pinning for better caching
3. **Lightweight alternatives**: Using `matplotlib-base` instead of full `matplotlib`
4. **Post-build cleanup**: Removes conda cache to reduce image size
5. **Consistent Python version**: Python 3.12 for reproducibility

## Build Times:

- **First build**: ~5-10 minutes (creating Docker image)
- **Cached builds**: ~1-2 minutes (when environment.yml unchanged)
- **Quick rebuild**: ~30-60 seconds (when only notebooks change)

## Tips:

- Don't modify `environment.yml` unless absolutely necessary
- Changes to notebooks don't trigger full rebuilds
- Tag releases for longer cache retention
