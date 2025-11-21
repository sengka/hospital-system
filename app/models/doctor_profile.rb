class DoctorProfile < ApplicationRecord
  belongs_to :user
  belongs_to :department
end
