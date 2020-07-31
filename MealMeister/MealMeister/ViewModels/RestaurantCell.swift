//
//  RestaurantCell.swift
//  MealMeister
//
//  Created by Brett Beattie on 7/30/20.
//  Copyright © 2020 Andrew Thomas. All rights reserved.
//

import UIKit

class RestaurantCell: UITableViewCell, Identifiable {
    @IBOutlet weak var displayNameLbl: UILabel!
    @IBOutlet weak var nameLbl: UILabel!
    @IBOutlet weak var tagLbl: UILabel!
    
    override func awakeFromNib() {
        super.awakeFromNib()
    }
    
    func configureCell(restaurant: Restaurant) {
        displayNameLbl.text = restaurant.displayName
        nameLbl.text = restaurant.name
        tagLbl.text = restaurant.tag
    }
}
