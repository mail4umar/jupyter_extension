import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { ILauncher } from '@jupyterlab/launcher';

import { LabIcon } from '@jupyterlab/ui-components';

const plugin: JupyterFrontEndPlugin<void> = {
  id: 'vertica-extension:plugin',
  autoStart: true,
  optional: [ILauncher],
  activate: (app: JupyterFrontEnd, launcher: ILauncher | null) => {
    if (launcher) {
      launcher.add({
        command: 'vertica-viewer:open',
        category: 'Other',
        rank: 1
      });
    }

    app.commands.addCommand('vertica-viewer:open', {
      label: 'Vertica Viewer',
      execute: () => {
        window.open('/voila/render/notebooks/vertica_viewer.ipynb', '_blank');
      }
    });
  }
};

export default plugin;