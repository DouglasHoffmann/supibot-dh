import fs from 'fs';
import path from 'path';

const commandsDir = './commands';
const results = new Map();

function walk(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            walk(fullPath);
        } else if (file.endsWith('.ts') || file.endsWith('.js')) {
            const content = fs.readFileSync(fullPath, 'utf-8');

            // Refined regex to handle multi-line and different quotes
            // Look for Name: "..." and Description: "..."
            const blocks = content.split(/declare\s*\(/);
            for (const block of blocks) {
                const nameMatch = block.match(/Name:\s*"(.*?)"/);
                const descMatch = block.match(/Description:\s*["']([\s\S]*?)["']\s*[,}]/);

                if (nameMatch) {
                    const name = nameMatch[1];
                    let description = 'No description found.';
                    if (descMatch) {
                        description = descMatch[1]
                            .replace(/\\"/g, '"') // unescape double quotes
                            .replace(/\\'/g, "'") // unescape single quotes
                            .replace(/\\\n/g, '') // remove escaped newlines
                            .replace(/\n/g, ' ')  // replace newlines with space
                            .replace(/\s+/g, ' ') // collapse spaces
                            .trim();

                        // Remove trailing backslash if any (artifact of some escaping)
                        if (description.endsWith('\\')) {
                            description = description.slice(0, -1).trim();
                        }
                    }

                    if (!results.has(name)) {
                        results.set(name, description);
                    }
                }
            }
        }
    }
}

walk(commandsDir);

const output = Array.from(results.entries()).map(([name, description]) => ({ name, description }));
console.log(JSON.stringify(output, null, 2));
