# Purge Unused Button

Purge Unused Button adds a one-click button to Blender's 3D Viewport tool header for removing orphaned data-blocks from the current file.

## Functionality

- Adds a button labeled **Purge Unsused Data** to the 3D Viewport tool header.
- Uses Blender's built-in `outliner.orphans_purge` operator.
- Displays the orphan-data icon so the control is easy to identify.
- Removes the button cleanly when the add-on is disabled or unregistered.

The add-on does not provide additional settings or a separate user interface. It simply exposes Blender's existing orphan-data purge operation directly in the 3D Viewport.

## Requirements

- Blender 4.2.0 or newer.

## Installation

1. Open Blender's **Preferences**.
2. Open the **Extensions** or **Add-ons** section, depending on your Blender version.
3. Choose **Install from Disk** and select this add-on's package or source folder.
4. Enable **Purge Unused Button**.

## Usage

1. Open a 3D Viewport.
2. Locate the **Purge Unsused Data** button in the tool header.
3. Click it to run Blender's orphan-data purge operation.

As with Blender's built-in purge command, review the data selected for removal before using it in a file where unused data may still be needed later.

## License

GPL-3.0-or-later
