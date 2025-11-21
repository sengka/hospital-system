describe('Hospital Appointment System Demo', () => {
    it('Demonstrates Patient, Doctor, and Admin flows', () => {
        // 1. Patient Flow - View Appointments
        cy.visit('/appointments');
        cy.wait(1000);
        cy.contains('Randevularım').should('be.visible');

        // Create New Appointment
        cy.contains('Yeni Randevu Al').click();
        cy.wait(500);
        cy.contains('Yeni Randevu Oluştur').should('be.visible');

        // Fill appointment form
        cy.get('select[name="appointment[doctor_id]"]').select(1); // Select first doctor
        cy.wait(500);

        // Set date and time
        const tomorrow = new Date();
        tomorrow.setDate(tomorrow.getDate() + 1);
        const dateTimeString = tomorrow.toISOString().slice(0, 16);
        cy.get('input[name="appointment[scheduled_at]"]').type(dateTimeString);
        cy.wait(500);

        cy.get('textarea[name="appointment[note]"]').type('Cypress demo randevusu - Test');
        cy.wait(500);

        cy.contains('Randevu Oluştur').click();
        cy.wait(1000);

        // Verify we're back at appointments list
        cy.url().should('include', '/appointments');
        cy.wait(1000);

        // 2. Doctor Flow
        cy.visit('/doctors/appointments');
        cy.wait(1000);
        cy.contains('Randevu Yönetimi').should('be.visible');

        // Check if there are appointments
        cy.get('table').should('be.visible');
        cy.wait(1000);

        // Try to update status if appointments exist
        cy.get('body').then(($body) => {
            if ($body.find('select[name="appointment[status]"]').length > 0) {
                cy.get('select[name="appointment[status]"]').first().select('confirmed');
                cy.wait(500);
                cy.contains('Güncelle').first().click();
                cy.wait(1000);
            }
        });

        // 3. Admin Flow - Doctors
        cy.visit('/admin/doctors');
        cy.wait(1000);
        cy.contains('Doktor Listesi').should('be.visible');

        // Verify doctors are listed
        cy.get('table').should('be.visible');
        cy.wait(1000);

        // Add new doctor
        cy.contains('Yeni Doktor Ekle').click();
        cy.wait(500);
        cy.contains('Yeni Doktor Ekle').should('be.visible');

        cy.get('input[name="user[name]"]').type('Dr. Cypress Test');
        cy.wait(300);
        cy.get('input[name="user[email]"]').type('cypress.test@example.com');
        cy.wait(300);
        cy.get('select[name="user[doctor_profile_attributes][department_id]"]').select(1);
        cy.wait(300);
        cy.get('input[name="user[doctor_profile_attributes][room_number]"]').type('999');
        cy.wait(500);

        cy.contains('Doktor Ekle').click();
        cy.wait(1000);

        // 4. Admin Flow - Departments
        cy.visit('/admin/departments');
        cy.wait(1000);
        cy.contains('Departman Listesi').should('be.visible');

        // Verify departments are listed
        cy.get('table').should('be.visible');
        cy.wait(1000);

        // Add new department
        cy.contains('Yeni Departman Ekle').click();
        cy.wait(500);
        cy.contains('Yeni Departman Ekle').should('be.visible');

        cy.get('input[name="department[name]"]').type('Cypress Test Departmanı');
        cy.wait(500);

        cy.contains('Departman Ekle').click();
        cy.wait(1000);

        // Final verification - go back to appointments
        cy.visit('/appointments');
        cy.wait(1000);
        cy.contains('Randevularım').should('be.visible');
    });
});
