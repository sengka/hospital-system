class User < ApplicationRecord
  has_secure_password
  enum :role, { patient: 0, doctor: 1, admin: 2 }

  has_one :doctor_profile
  has_many :patient_appointments, class_name: 'Appointment', foreign_key: 'patient_id'
  has_many :doctor_appointments, class_name: 'Appointment', foreign_key: 'doctor_id'
  
  accepts_nested_attributes_for :doctor_profile
end
