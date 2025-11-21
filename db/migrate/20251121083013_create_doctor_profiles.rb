class CreateDoctorProfiles < ActiveRecord::Migration[8.1]
  def change
    create_table :doctor_profiles do |t|
      t.references :user, null: false, foreign_key: true
      t.references :department, null: false, foreign_key: true
      t.string :room_number
      t.text :bio

      t.timestamps
    end
  end
end
