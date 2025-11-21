// Cypress support file
import './commands';

// Ignore uncaught exceptions from the application (e.g., importmap issues)
Cypress.on('uncaught:exception', (err, runnable) => {
    // returning false here prevents Cypress from failing the test
    return false;
});
