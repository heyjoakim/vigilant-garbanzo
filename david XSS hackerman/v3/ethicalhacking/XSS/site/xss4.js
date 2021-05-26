import { shell } from 'electron';
import path from 'path';

shell.openPath(path.join(__dirname, 'test.docx'));