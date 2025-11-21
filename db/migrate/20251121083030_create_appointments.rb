class CreateAppointments < ActiveRecord::Migration[8.1]
  def change
    create_table :appointments do |t|
      t.integer :patient_id
      t.integer :doctor_id
      t.datetime :scheduled_at
      t.integer :status
      t.text :note

      t.timestamps
    end
  end
end
