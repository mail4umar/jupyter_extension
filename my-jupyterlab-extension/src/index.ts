import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { INotebookTracker } from '@jupyterlab/notebook';

const plugin: JupyterFrontEndPlugin<void> = {
  id: 'my-jupyterlab-extension',
  autoStart: true,
  requires: [INotebookTracker],
  activate: (app: JupyterFrontEnd, notebookTracker: INotebookTracker) => {
    console.log('JupyterLab extension is activated!');
    
    app.commands.addCommand('voila:open', {
      label: 'Open Voilà Notebook',
      execute: () => {
        const widget = notebookTracker.currentWidget;
        if (widget) {
          const notebookPath = widget.context.path;
          const voilaUrl = `/voila/render/${notebookPath}`;
          window.open(voilaUrl, '_blank');
        } else {
          console.error('No notebook is active.');
        }
      }
    });

    app.commands.notifyCommandChanged();
  }
};

export default plugin;
